export default {
  layout: "article.njk",
  tags: ["posts"],
  permalink: data => {
    const date = new Date(data.date);
    const path = date.toISOString().slice(0, 10).replaceAll("-", "/");
    return `/${path}/${data.page.fileSlug}/`;
  }
};
