# custom-product-recommender-skill

> **GenPark AI Agent Skill** -- Shopping quiz recommendation matching builder.

## Quick Start

```python
from client import CustomProductRecommenderClient
client = CustomProductRecommenderClient()
res = client.match_quiz({"skin": "oily"}, [{"id": "1", "tags": ["oily"]}])
print(res["recommended_product_id"])
```
