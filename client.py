"""
custom-product-recommender-skill: Client SDK
Auto-maps quiz input tags against catalog products to recommend targeted solutions.
"""
from __future__ import annotations
from typing import Optional


class CustomProductRecommenderClient:
    """
    SDK for quiz matching pipelines.
    """

    def match_quiz(
        self,
        quiz_responses: dict,
        catalog: list[dict],
    ) -> dict:
        answers = {str(v).lower() for v in quiz_responses.values()}
        
        best_product = None
        max_matches = 0

        for p in catalog:
            pid = p.get("id", "unknown")
            p_tags = {str(t).lower() for t in p.get("tags", [])}

            overlap = len(answers.intersection(p_tags))
            if overlap > max_matches:
                max_matches = overlap
                best_product = pid

        # Confidence percentage
        total_q = max(1, len(quiz_responses))
        confidence = (max_matches / total_q) * 100.0

        return {
            "recommended_product_id": best_product or (catalog[0].get("id") if catalog else None),
            "match_percentage": round(confidence, 1)
        }
