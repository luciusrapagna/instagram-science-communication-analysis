# Data dictionary

The public dataset contains one row per Instagram post.

| Variable | Type | Description |
|---|---|---|
| `record_id` | string | Anonymous sequential record identifier |
| `project` | categorical | Extension project: Ocean Culture or PsicoCampus |
| `publication_month` | string | Publication month in `YYYY-MM` format |
| `post_type` | categorical | Image, Carousel, or Reel |
| `duration_seconds` | numeric | Platform-exported post duration in seconds |
| `views` | integer | Number of recorded views |
| `reach` | integer | Number of accounts reached; two values are missing |
| `likes` | integer | Number of likes |
| `shares` | integer | Number of shares |
| `comments` | integer | Number of comments |
| `saves` | integer | Number of saves |
| `follows` | integer | Number of follows attributed by the platform; two values are missing |
| `total_interactions` | integer | Likes + shares + comments + saves |

## Missing data

Missing values are represented by empty CSV fields. They must not be treated
as zeros. Analyses use available observations for each outcome.

## Derived measures

The analysis calculates:

```text
interactions_per_100_reached = total_interactions / reach * 100
likes_per_100_reached = likes / reach * 100
```

These measures are counts per 100 accounts reached, not percentages of unique
users who interacted.

## Privacy transformations

The public dataset excludes post identifiers, account identifiers, usernames,
account names, descriptions, permanent links, exact dates, and exact times.
