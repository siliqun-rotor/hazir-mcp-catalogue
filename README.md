# Hazir MCP catalogue

Reviewed **metadata** for MCP integrations used by Hazir / Siliqun Rotor marketplace discovery.

- Licence of this catalogue metadata: **Apache-2.0**
- Registry metadata is not an executable install path
- Initial revision: see `docs/accepted-revision-r1.json` (fixture scope)
- Contribution guide: `CONTRIBUTING.md`

Org: `siliqun-rotor` (owner T-103).

## Studio integration bundles

[integrations/catalog.json](integrations/catalog.json) contains reviewed Studio archive descriptors alongside the predecessor MCP registry metadata. Each ZIP is pinned to a publisher commit, archive SHA-256 and canonical bundle SHA-256. Hazir verifies the full payload inventory and loads declarations as data; installation requires access to the destination native project and its own Vault connections. No provider credentials or grants are distributed here.

The Studio publish-integration command publishes a verified export to its existing publisher repository and updates this index by stable ID. Repeated publication preserves one current entry; changed digests retain predecessor descriptors.
