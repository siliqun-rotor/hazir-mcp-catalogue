# Contributing to the Hazir integration catalogue (draft — T-203)

**Status:** Draft under `cursor`. Public repository destination and license are **owner-reserved (T-103)** and not created by this document.

## What this catalogue is

Reviewed **metadata** for MCP integrations (upstream-compatible `server.json` + `hazir.json` overlay). It is not an executable install path, not a second MCP registry protocol, and not a transfer of customer credentials.

## Submissions

1. Add `integrations/<stable_id>/server.json` (upstream-compatible) and `hazir.json` (`hazir.catalogue.overlay/1`).
2. Do not put secrets, private endpoints, tokens, or customer IDs in PRs.
3. Do not self-assert readiness or company-verified badges.
4. Declare license/provenance for the listing metadata; listed services keep their own licenses.

## Automated checks (untrusted PR)

- Schema/overlay validation (`impl/validate_manifest.py` predicates).
- Secret-marker and active-markup rejection.
- Duplicate `stable_id` rejection.
- No `npm install` / package lifecycle / arbitrary commands on contributor artifacts.
- CI must not receive production credentials.

## Review

- Platform reviewer accepts immutable catalogue revisions (T-204).
- Publisher claims (T-302) change listing maintenance authority only.
- Withdrawal retains history (T-304).

## Destination

Owner-approved (T-103, 2026-10-30): GitHub org `siliqun-rotor`, catalogue metadata under **Apache-2.0**. Exact repository name to be created under that org when publication is separately authorized (T-801). This guide is normative for L0 checks and contribution shape before the remote exists.
