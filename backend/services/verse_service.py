import random

VERSES = [

    {
        "reference": "John 3:16",
        "text": (
            "For God so loved the world that He gave "
            "His one and only Son, that whoever believes "
            "in Him shall not perish but have eternal life."
        )
    },

    {
        "reference": "Philippians 4:13",
        "text": (
            "I can do all things through Christ "
            "who strengthens me."
        )
    },

    {
        "reference": "Psalm 23:1",
        "text": (
            "The Lord is my shepherd; "
            "I shall not want."
        )
    },

    {
        "reference": "Proverbs 3:5-6",
        "text": (
            "Trust in the Lord with all your heart "
            "and lean not on your own understanding; "
            "in all your ways submit to Him, "
            "and He will make your paths straight."
        )
    },

    {
        "reference": "Romans 8:28",
        "text": (
            "And we know that in all things "
            "God works for the good of those "
            "who love Him, who have been called "
            "according to His purpose."
        )
    }

]


def get_daily_verse():
    return random.choice(VERSES)