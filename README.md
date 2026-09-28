\# Public Website Scraper



A scraper that turns any public web page into structured JSON. It loads the page in a real headless browser, so JavaScript-rendered content is captured, then asks an OpenAI model to extract the data into clean fields.



\## How it works



1\. \*\*Scrape:\*\* `scraper.py` opens the URL in headless Chromium (Playwright) and returns the page's rendered text.

2\. \*\*Extract:\*\* the text is sent to `gpt-4o-mini` with JSON mode enabled, so the response is always valid JSON.

3\. \*\*Parse:\*\* the JSON is converted into a Python dictionary and printed.



The prompt is generic. The model chooses field names based on what is on the page (quotes, products, articles and so on), and you can optionally pass an `extraction\_goal` such as "Extract product names and prices" for more precise results. Long pages are trimmed to a character limit to control cost.



\## Setup



```bash

pip install playwright openai python-dotenv

playwright install chromium

```



Create a `.env` file in the project folder:



```

OPENAI\_API\_KEY=your-key-here

```



\## Usage



Open `Exercise1\_test.ipynb` and run the cells from top to bottom. Change `url\_to\_test` (and optionally `goal`) in the last cell.



Tested on:

\- `https://quotes.toscrape.com/js/` (content loaded by JavaScript)

\- `https://www.seedprod.com/best-blogging-platforms/` (a long article page heavy with trackers)



\## Problems I ran into and how I solved them



\- \*\*Playwright crashed inside Jupyter on Windows\*\* (`NotImplementedError`). Jupyter's event loop on Windows can't start the browser subprocess. Fix: I moved Playwright into a standalone script, `scraper.py`, and the notebook runs it as a separate process with `subprocess.run`.

\- \*\*`UnicodeDecodeError` from curly quotes.\*\* Windows defaults to cp1252. Fix: I forced UTF-8 on both the script's output and the notebook's decoding.

\- \*\*Page load timeout on tracker-heavy sites.\*\* `wait\_until="networkidle"` never finishes on pages that keep making background requests. Fix: I switched to `domcontentloaded`.



\## Limitations



\- Pages that need clicking, scrolling or pagination only return the first view of content.

\- Pages behind a login are not supported.

\- Very long pages are trimmed to a character limit.

\- Output quality depends on the model, so check important results.



\## Security note



Your API key lives in `.env`, which is excluded from the repo through `.gitignore`. Never commit it.

