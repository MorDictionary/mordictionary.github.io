# 🧠 MorDictionary

**Defining everything from neologisms to hyperspecific phrasings.**
A living, digital dictionary by the Moribund Institute — exploring language, invention, and meaning in the modern age.

---

## 🌐 Live Site

👉 [https://mordictionary.github.io](https://mordictionary.github.io)

---

## 📖 About

MorDictionary is an open, evolving lexicon of original terms, definitions, and linguistic curiosities.
Each entry is designed in a themed format — blending etymology, humor, philosophy, and aesthetics.

**Example entries:**

* **Schrödinger’s Gay** — The paradox of uncertain orientation under technological mediation
* **Xenoestrogen** — A “foreign estrogen” disrupting natural hormonal balance
* *(more coming soon…)*

---

## 🏗️ Built With

* [Hugo](https://gohugo.io/) — Static site generator
* [hugo-brewm](https://github.com/foxihd/hugo-brewm) — Theme
* Markdown + HTML hybrid content
* Hosted on [GitHub Pages](https://pages.github.com/)
* Optional support for Cloudflare R2 or external image hosting

---

## ⚙️ Local Setup & Deployment

### 🧩 Requirements

* [Hugo (extended version)](https://gohugo.io/getting-started/installing/)
* Git
* Python 3 (for the image sorter script)

### 🧱 Build and Run Locally

```bash
# Clone the repo
git clone https://github.com/mordictionary/mordictionary.github.io.git
cd mordictionary

# Run Hugo development server
hugo server -D
```

Then visit 👉 [http://localhost:1313](http://localhost:1313)

### 🚀 Deploy to GitHub Pages

```bash
# Build static site
hugo -d public

# Commit and push
git add .
git commit -m "Rebuild site"
git push origin main
```

---

## 🗂️ File Overview

| Folder            | Purpose                                |
| ----------------- | -------------------------------------- |
| `/content/`       | Markdown files for dictionary entries  |
| `/static/images/` | Organized images (Dewey Decimal + A–Z) |
| `/themes/`        | Hugo theme files                       |
| `/layouts/`       | Custom HTML layouts                    |
| `/archetypes/`    | Content blueprints                     |
| `/unsorted/`      | Drop new images here before sorting    |
| `/scripts/`       | Utility scripts (e.g., image sorter)   |

---

## 🧭 Project Workflow

### 🖼️ Image Sorting System

Images are organized according to the **Dewey Decimal Classification** and alphabetically under `/static/images/`.

#### Folder Structure

```
static/images/
├── 000_General-Knowledge/
│   ├── A/
│   ├── B/
│   └── ...
├── 400_Language/
│   ├── A/
│   ├── B/
│   └── ...
```

#### Naming Convention

```
<Name>_<Letter>-<Dewey>.ext
```

**Example:**

```
Irrefragable Definition_I-400.webp
Etymology Roots_E-400.png
```

#### Automatic Sorting Script

```bash
# Make executable
chmod +x sort_images.py

# Optional dry run (preview what it will do)
./sort_images.py --dry-run

# Move or copy files from unsorted → static/images
./sort_images.py
```

> 📂 Place all new images into the `/unsorted/` folder before sorting.
> The script automatically detects the `Letter-Dewey` tag and places it in the correct folder.

---

### 📝 Creating New Dictionary Entries

To create a new entry:

```bash
hugo new content/dictionary/irrefragable.md
```

Then edit the file at `/content/dictionary/irrefragable.md`:

```yaml
---
title: "Irrefragable"
date: 2025-11-06
description: "Impossible to refute or contradict; indisputable."
image: "/images/400_Language/I/Irrefragable Definition_I-400.webp"
---
```

And fill in your entry with Markdown + HTML hybrid formatting:

```html
<div class="themed-dict-entry">
  <h3>Irrefragable</h3>
  <p><em>Adjective</em></p>
  <p>Impossible to refute or contradict; indisputable.</p>
  <p><strong>Example:</strong> The evidence was irrefragable, leaving no doubt of his innocence.</p>
</div>
```

---

## 🧰 Useful Commands

```bash
# Preview site locally
hugo server -D

# Build site for deployment
hugo -d public

# Clean up old builds
rm -rf public/

# Run image sorting
./sort_images.py
```

---

## ⚖️ License

* **Code and site structure:** MIT License
* **Content (entries, text, images):** Creative Commons Attribution 4.0 (CC-BY 4.0)

  * You may share or adapt entries with credit to **MorDictionary / Moribund Institute**.

---

## 🤝 Contributing

Contributions are welcome!
If you’d like to suggest a word, definition, or edit, open an **Issue** or **Pull Request**.

**Guidelines:**

1. Keep entries concise, well-formatted, and thematically consistent.
2. Use the `<div class="themed-dict-entry">` structure for new entries.
3. Include etymology or example sentences when possible.
4. Use proper Markdown or inline HTML for stylistic control.

---

## ☕ Acknowledgments

* **Murdoch Maxwell** — Founder / Lexicographer-in-chief
* The **Moribund Institute** — For ongoing inspiration and linguistic mischief

---

> “Words are time capsules for thought.”
> — *MorDictionary Manifesto*

```

---
