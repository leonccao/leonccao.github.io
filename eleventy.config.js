export default function (config) {
  config.addPassthroughCopy("src/assets");
  config.addPassthroughCopy({ "images/favicon.png": "images/favicon.png" });
  config.addFilter("dateLabel", value => new Intl.DateTimeFormat("en", {
    year: "numeric", month: "short", day: "numeric", timeZone: "UTC"
  }).format(new Date(value)));
  config.addFilter("dateISO", value => new Date(value).toISOString().slice(0, 10));
  config.addCollection("writing", api => api.getFilteredByTag("posts")
    .filter(item => item.data.listed !== false).sort((a, b) => b.date - a.date || b.fileSlug.localeCompare(a.fileSlug)));
  return { dir: { input: "src", output: "_site" }, markdownTemplateEngine: false, htmlTemplateEngine: false };
}
