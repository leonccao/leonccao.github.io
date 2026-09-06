# Leon Cao’s personal lab

Live site: https://leonccao.github.io/

An English personal site for learning, projects, and writing. Built with Eleventy,
Markdown, Nunjucks templates, and plain CSS. No browser JavaScript is required.

## Develop and check

Use Node.js 24 or newer and Python 3.9 or newer.

```sh
npm ci
npm run dev
```

Open the local address printed by Eleventy (normally http://localhost:8080/).

```sh
npm run build
npm test
```

The build creates `_site/`, which is not committed. Tests check internal links and
anchors, image descriptions, preserved legacy article bodies, and Markdown
publishing in an isolated temporary build. The sample never enters the live build.

## Write a post

Copy `examples/new-post.md` into `src/posts/` with a descriptive filename, such as
`my-experiment.md`. Edit its title, date, description, tags, and body. The default
URL is `/YYYY/MM/DD/my-experiment/`, using the post date in UTC. Posts automatically
appear on the homepage and in the archive, newest first. Set `listed: false` to
exclude a post from listings; this does not make its URL private. Keep unfinished
work outside `src/posts/` until it is ready to publish.

Add `permalink: /your-existing-path/` to preserve a specific URL. The `OS` tag adds
the post to `/tags/OS/`; other tags are metadata without generated tag pages.
Place images in `src/assets/` and reference them as `/assets/filename` with alt text.
Markdown is not interpreted as a template, so code containing template syntax is safe.

## Edit the site

- Introduction and identity: `src/_data/site.json`.
- Project descriptions, links, and illustration text: `src/_data/projects.json`.
- Shared layouts: `src/_includes/`. Homepage: `src/index.njk`.
- Styling and original concept illustrations: `src/assets/`.

The illustrations explain concepts; they do not represent benchmark results.
Project descriptions identify course learning work rather than production products.

## Publish

GitHub Pages uses **GitHub Actions** as its publishing source. A push to `master`
builds and tests the site, uploads only `_site/`, then deploys it. Pull requests
build and test without deploying. Review the “Build and deploy personal lab” run
in the repository’s Actions tab if publishing fails. No additional hosting account,
CMS, or deployment secret is needed.

## Preserved articles and recovery

The three original 2018 article bodies are retained as HTML content with explicit
permalinks and shared layouts. Their code, tables, and heading anchors remain
unchanged; `scripts/fixtures/legacy-articles.json` records their original body hashes.
Hello World remains accessible at its original URL but is not listed. New posts
should use Markdown. If intentionally editing a legacy article, update its baseline
hash after reviewing the content change.

Older theme assets remain in Git for reference but are not copied to the new site.
The last working pre-redesign commit is `3ec051184dc8b76c2bad04da85fa48d9601c38b5`.
For emergency rollback, restore that tree in a new commit, then set Pages back to
**Deploy from a branch**, `master`, root `/`, and verify the resulting deployment.
