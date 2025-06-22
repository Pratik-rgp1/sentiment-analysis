from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test with a positive sentiment text
        result = sentiment_analyzer("I love programming!")
        self.assertEqual(result['label'], 'positive')
        self.assertGreater(result['score'], 0.5)

        # Test with a negative sentiment text
        result = sentiment_analyzer("I hate bugs in my code.")
        self.assertEqual(result['label'], 'negative')
        self.assertLess(result['score'], -0.5)

        # Test with a neutral sentiment text
        result = sentiment_analyzer("The sky is blue.")
        self.assertEqual(result['label'], 'neutral')
        self.assertAlmostEqual(result['score'], 0.0, delta=0.1)

unittest.main()