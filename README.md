# Minty personal blog

Live site: https://leonccao.github.io/

This repository contains the generated HTML, CSS, JavaScript, and images from
an existing Hexo blog. The original Hexo source and configuration are not included;
no build or dependency installation is required to publish these files.

## Publishing

GitHub Pages serves the root of the `master` branch using **Deploy from a branch**.
Push changes to `master` to publish. `.nojekyll` preserves the prebuilt static files.
Use root-relative internal asset and page URLs, such as `/css/style.css` and `/archives/`.

The repository is named `leonccao.github.io` to publish at the account root.
The former `https://mintycc.github.io/` address belongs to the old account name.
Pages previously referenced a missing `gh-pages` branch; it now publishes `master`.
Navigation to absent About, Links, and Atom feed files has been removed.

## Local preview

From this checkout directory:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000/.
