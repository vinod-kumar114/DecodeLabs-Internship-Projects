# Project 3: AI Recommendation Logic

**DecodeLabs Artificial Intelligence Internship — Batch 2026**

## Goal
Create a simple recommendation system based on user preferences.

## Requirements Covered
- ✅ Take user input (favorite genres)
- ✅ Match preferences using similarity logic (genre overlap score)
- ✅ Display recommended items (top 5 ranked movies)

## How to Run
```bash
python recommender.py
```
Enter your favorite genres (e.g. `action, sci-fi`) when prompted, and the
program will suggest the top matching movies from its catalog.

## How It Works
Each movie has a set of genre tags. The user's chosen genres are compared
against every movie's tags using a simple similarity score (the number of
overlapping genres). Movies are ranked by this score, and the top matches
are shown as recommendations.

## Skills Demonstrated
Logic building, pattern matching, recommendation concepts.
