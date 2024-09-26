import unittest
from src.llm_integration.openai_client import get_openai_response

class TestOpenAIClient(unittest.TestCase):
    def test_openai_response(self):
        response = get_openai_response("Test prompt")
        self.assertTrue(len(response) > 0)
