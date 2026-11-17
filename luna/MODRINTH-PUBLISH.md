# Putting Luna on Modrinth — the real process

Status: **not published.** Nothing is uploaded yet; this file is the checklist to do it from.
Sources are Modrinth's own help center, its v2 API docs, and Fabric's loader docs.

## What file to attach

Attach **`import-ready/luna/luna-fabric-1.20.1-0.0.3.jar`** (35,293 bytes, sha256 22bd3069e69ea1,
built 2026-11-16). The
file name follows the convention the other Homestead jars already use — `carycon-fabric-1.20.1-2.1.2.7.jar`,
`celestconfig-fabric-1.20.1-1.1.2.jar`, `balm-fabric-1.20.1-7.3.3.jar`, `chipped-fabric-1.20.1-3.0.7.jar` —
that is `<mod id>-fabric-<game version>-<mod version>.jar`, so the loader, the game version and the
version are readable straight off the name. What the loader actually reads is the manifest **inside**
the jar, which still says id `luna` and version `0.0.3`; the file name is only ever the human-facing
label, so renaming it changes nothing about how the mod loads.

Inside that jar `fabric.mod.json` sits at the **archive root** (Fabric's loader rule is the only
archive-layout rule that exists: the manifest may not sit one folder deep
— <https://docs.fabricmc.net/develop/loader/fabric-mod-json>) together with `META-INF/MANIFEST.MF`,
`com/example/Luna.class`, `com/example/LunaSpawnEgg.class` and `assets/luna/...` (the icon, the
language file, the item model, her 512x256 coat and the egg icon). Modrinth accepts `.jar`, `.zip`,
`.mrpack` and `.litemod` as version files (<https://docs.modrinth.com/api/operations/createversion/>),
so the jar goes straight in. `import-ready/luna-modrinth.zip` is the same entries plus `CHANGES.html`
for the case where you want a `.zip`; the jar is the preferred file.

Source is public now: the repository lives at <https://github.com/UOElliot54/luna-fabric>, so the
page's `source_url` and Links panel should carry it, and the jar's own manifest carries a matching
`contact` block. Note the two specs use different names for the same thing: a `fabric.mod.json` has
no `source_url` key at all — under Fabric's v1 spec the key is `contact`, whose defined members are
`email`, `irc`, `homepage`, `issues` and `sources` (<https://wiki.fabricmc.net/documentation:fabric_mod_json_spec>);
`source_url` is a Modrinth-side field on the version, not a manifest field. Adding a manifest
`contact` block means rebuilding the jar, so the correct file to attach is the newest one above, and
you fill the page links and the jar in one pass.

## If you already uploaded a version and the file changed

A hosted version's file cannot be edited in place, and two versions on one project cannot share a
version number. So replacing a file means one of:

- **delete that version, then create a new one with the same number** (`0.0.3`) carrying the new
  file — the version number keeps matching the manifest inside the jar, which is what you want;
  deleting and re-submitting sends the project back through the moderation queue;
- **keep the live version and add a second one** — the number has to be unique, so `0.0.4`, and the
  manifest inside the new jar has to say `0.0.4` too, which means another rebuild and a renamed file.

If the version is still sitting in review or a draft, nothing is live yet and you simply submit the
newest file once — there is nothing to replace.

## Account

A normal free Modrinth account is enough — sign up with Discord, GitHub, Microsoft, Google, Steam,
GitLab or a password; GitHub linking is just one more optional sign-in method
(<https://support.modrinth.com/en/articles/8793347-add-more-authentication-methods-to-an-account>).
There is no author-claim or "verify before publishing" step you have to pass. The "verified" badge
you sometimes see on other people's pages is staff-side authorship confirmation, has no documented
effect on publishing, and nothing you upload grants it.

## Values to enter

| Field | Value for this mod |
| --- | --- |
| Project type | Mod |
| Slug | `luna-the-maine-coon-cat` — free today (modrinth.com/mod/luna-the-maine-coon-cat returns "Project not found"). Plain `luna` is **taken** (modrinth.com/mod/luna is someone else's mod). Slugs are 3–64 chars of that pattern and are mutable; the 8-character project ID is the stable one, and you can test availability with `GET /v2/project/{slug}/check` (<https://docs.modrinth.com/api/operations/checkprojectvalidity/>) |
| Title | `Luna` (or whatever you want readers to see — note the manifest's own `name` inside the jar still reads `Luna - The Maine Coon (Homestead Trial)`, which is what the loader shows in its own listings) |
| Description | One or two sentences, then the body: what the egg does, that she behaves like a vanilla cat, that the coat is her real pattern |
| `license_id` | `MIT` — matches the manifest's `license` (changed from `CC0-1.0` because the source is going public, and an all-rights-reserved or CC0 tag would contradict a public repository); the repo's `LICENSE` file says MIT too. Caveat to keep in the description: her coat texture descends from Minecraft's own cat texture, so MIT covers your code and your own art, not Mojang's assets |
| `loaders` | `["fabric"]` |
| `game_versions` | `["1.20.1"]` — the version Homestead pins; widen it only if you test on others |
| `environment` | `client_and_server` (she works singleplayer and on a server alike) |
| Version name / number | `0.0.3` — semver is what Modrinth's version field wants (<https://support.modrinth.com/en/articles/8793369-version-number-recommendations>) |
| `version_type` | `release` |
| Changelog | the text from `luna/CHANGES.html` |
| Dependencies | Fabric API as **optional** (`dependency_type: optional`) — our jar pulls in no fabric-api classes at all, but Homestead ships it through The Ultimate Compat Mod, so declaring it optional is the honest statement. Every version has to state its dependencies (<https://modrinth.com/legal/rules>) |
| Icon / gallery | `assets/luna/icon.png` (the pixel-art face) plus in-game screenshots if you want |
| `source_url` | `https://github.com/UOElliot54/luna-fabric` — the repository is public. The Links panel takes the same pair: Source code = that URL, Issue tracker = `<repo>/issues`; Wiki page and Discord invite stay blank unless you have them. The jar's manifest already repeats both links in its `contact` block (`sources` and `issues`), so the page and the file agree without anyone editing either |

## What happens after you submit

You submit it yourself, but it enters a human moderation queue and shows as "Under review" until a
moderator approves it. Modrinth aims at 24–48 hours for projects (72–96 hours for modpacks) but says
real waits have stretched to two weeks or more while moderators are re-trained, and there is no
queue-position display (<https://support.modrinth.com/en/articles/8793355-project-review-times>).
Newly uploaded files also sit in a `processing` state while Modrinth validates that the archive is a
real Minecraft mod, and an archive whose manifest is not recognized gets rejected — you fix the
layout and re-upload, which puts you at the end of the queue (<https://docs.modrinth.com/api/>).
Their moderation notes mention an in-house malware detector that can force a manual technical
review; the exact scanner behaviour and what happens on a failed scan are **not documented**, so do
not plan around a specific outcome. Do not delete an old version and re-upload it, that also resets
your queue position.

## Getting her into Homestead itself on Modrinth

That is Tokimi's decision, not yours: a modpack may only reference files already hosted on Modrinth
(or the four whitelisted git hosts), so you cannot hand them an un-uploaded jar
(<https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack>). Permission for
someone else's content in a Modrinth pack is satisfied by any of: the project is already hosted on
Modrinth, an open-source license, a statement in that project's own description, or the author's
written yes (screenshot goes in the pack's "Moderation" tab)
(<https://support.modrinth.com/en/articles/8797527-obtaining-modpack-permissions>). Publishing Luna
standalone first is the clean route: it grants Modrinth the right to list her in packs, and Tokimi
then just adds her as a dependency of a new Homestead version. Homestead is a `.mrpack`, so any
pack edit happens in that format (export from Modrinth App, or packwiz/Pakku/MC-Modpack-Kit if you
edit it by hand).

## Doing it yourself, in order

1. Sign up, pick the slug, fill the fields above on the project page.
2. Attach `import-ready/luna/luna-fabric-1.20.1-0.0.3.jar` as the version's primary file.
3. Set `loaders`, `game_versions`, `environment`, `version_number`, `version_type`, dependencies.
4. Submit with status public → watch for `processing`, then "Under review", then live.
5. If rejected, the moderator message says what rule or metadata problem it hit; fix that, do not
   re-upload the same archive.

Upload size is nowhere near an issue: our archive is 35 KB. The size ceiling itself is **not
documented** (a user report quotes an upload UI complaining at 500 MiB for a modpack), so treat it
as a non-factor for this mod.
