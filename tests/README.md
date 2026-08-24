# Tests

Real-browser tests. They drive the built `index.html` through Chromium and assert
on what the page actually renders, which is how most of the bugs in this project
were found.

## Running them

```bash
cd tests
npm install                 # pulls Playwright
npx playwright install chromium

# in one terminal — serve the repo root
npm run serve

# in another
npm run cart
npm run reminders
# ...or any script listed in package.json
```

Serve over **HTTP, not `file://`**. Browsers partition storage differently for
`file://` origins and the reminder tests give false failures there.

`BASE_URL` overrides the address if you serve on a different port.

## What each one covers

| Script | Covers |
|---|---|
| `gate` | Sign-in, passcode encryption, unlock, wrong passcode, lock/unlock round trip |
| `reminders` | 1-day and 30-minute reminders firing, no duplicates after reload, routing |
| `deletes` | Deleting tasks from the list, the edit sheet, and the Done filter; persistence |
| `ghosts` | Reminders disappearing along with the thing they pointed at |
| `legacy` | Cleaning up reminders saved before they carried a reference |
| `library` | Ingredient search, cuisine and category filters, the nutrition card |
| `cart` | Drag into and out of the cart, own items, ticking off, reload, emptying |
| `planner` | Meal drag-and-drop, grocery aggregation, calendar entries |
| `names` | Task names staying legible on the calendar at every width |

Screenshots land in `tests/screenshots/`.
