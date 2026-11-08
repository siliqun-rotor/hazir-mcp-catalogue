# Slack briefing actions

Portable, data-only declaration bundle for customer-selected Slack accounts.
No workspace, channel, credential, Vault reference or grant is packaged.
Install the reviewed bundle in Hazir Genie, choose actions, connect the customer's
Vault credential to `https://slack.com/api`, then approve the exact outbound item.
Scopes are declared per action. Slack's JSON `ok: false` is a failure even on HTTP 200.
List public channels using `types=public_channel`; follow cursors explicitly.
Message delivery and history depend on the Slack app's scopes and channel access.
These declarations do not assert live provider acceptance or a verified badge.

Primary method references checked 2026-11-08:
- https://docs.slack.dev/reference/methods/auth.test/
- https://docs.slack.dev/reference/methods/conversations.list/
- https://docs.slack.dev/reference/methods/chat.postMessage/
- https://docs.slack.dev/reference/methods/conversations.history/

`python3 bundles/slack-web-api/build.py` reproduces the checksum-pinned archive.
Catalogue metadata and authored declarations: Apache-2.0. Slack retains its own
service terms and trademarks. Payload code is inert guidance; the loader never executes it.
