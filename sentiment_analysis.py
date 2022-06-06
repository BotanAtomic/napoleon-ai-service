from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",
                            return_all_scores=True)


def sentiment_analysis(data):
    return sentiment_pipeline(data)


def emotion_analysis(data):
    emotions = emotion_pipeline(data)[0]
    value = {}
    for emotion in emotions:
        value[emotion["label"]] = emotion["score"]
    return [value]
