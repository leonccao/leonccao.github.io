# Minty personal blog

Live site: https://leonccao.github.io/mintycc.github.io/

This repository contains the generated HTML, CSS, JavaScript, and images from
an existing Hexo blog. The original Hexo source and configuration are not included;
no build or dependency installation is required to publish these files.

## Publishing

GitHub Pages serves the root of the `master` branch using **Deploy from a branch**.
Push changes to `master` to publish. `.nojekyll` preserves the prebuilt static files.
Keep internal asset and page URLs under `/mintycc.github.io/`, the project URL prefix.

The former `https://mintycc.github.io/` address does not serve this repository under
the current `leonccao` account. Pages previously referenced a missing `gh-pages`
branch, and the HTML used root-level paths that broke at the project URL.
Navigation to absent About, Links, and Atom feed files has been removed.

## Local preview

From the parent directory of this checkout:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000/mintycc.github.io/ so the project URL prefix is preserved.
