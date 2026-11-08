"""Build a data-only portable bundle; accounts and grants are destination-local."""
import hashlib,io,json
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
def encoded(value,pretty=False):return json.dumps(value,ensure_ascii=False,**({'indent':2}if pretty else {'separators':(',',':')})).encode()
tools=json.loads((Path(__file__).parent/'tools.json').read_text())
flow={'key':'slack_connect','entry':'configure','max_loops':1,'nodes':{'configure':{'kind':'ask','next':'respond'},'respond':{'kind':'respond'}}}
files={
 'tools.json':encoded(tools,True),'flow.json':encoded(flow,True),'teach.json':b'[]',
 'fixtures/response.json':encoded({'fixture':True,'message':'No provider run is included. Connect your account and verify in Hazir Genie.'},True),
 'transforms/pre.zs':b'input','transforms/post.zs':b'input',
 'code/siliq-graph.json':encoded(flow,True),
 'code/client.py':b'import os\nfrom siliqun_rotor import SiliqunRotorClient\nclient = SiliqunRotorClient(base_url=os.environ["SQR_BASE_URL"],api_key=os.environ["SQR_API_KEY"])\nprint(client.run_project_flow(os.environ["SQR_PROJECT_ID"],os.environ["SQR_TASK"]))\n',
 'code/client.ts':b'// Run the installed flow with your destination SDK and project access.\n// Provider credentials are resolved by the destination Vault, not this bundle.\n',
 'code/request.sh':b'#!/bin/sh\n# Call your installed project through its native authenticated runtime.\n# This archive contains no account, destination grant or provider credential.\n',
}
manifest={'$schema':'https://sqrengine.com/schemas/bundle/v1.json','name':'slack-web-api','displayName':'Slack briefing actions','version':'1.0.0','author':'Siliqun Rotor Community','license':'Apache-2.0','description':'Choose Slack identity, public channel listing, approved message delivery and readback actions. Connect your own account through destination Vault.','category':'Integrations','entryFlow':flow['key'],'toolsCount':len(tools),'inventory':[{'path':p,'byteLength':len(b),'sha256':sha(b)}for p,b in sorted(files.items())],'createdAt':'2026-11-08T00:00:00Z'}
manifest['bundleSha256']=sha(encoded(manifest));files['manifest.json']=encoded(manifest,True)
out=io.BytesIO()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)as z:
 for name,data in sorted(files.items()):
  info=zipfile.ZipInfo(name,date_time=(2026,11,8,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data)
data=out.getvalue();dest=ROOT/'dist';dest.mkdir(exist_ok=True);archive=manifest['bundleSha256']+'.sqr-bundle.zip';(dest/archive).write_bytes(data)
release={'archive':'dist/'+archive,'bundleSha256':manifest['bundleSha256'],'archiveSha256':sha(data),'toolsCount':len(tools)}
(Path(__file__).parent/'release.json').write_bytes(encoded(release,True)+b'\n');print(json.dumps(release))
