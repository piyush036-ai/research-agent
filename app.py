import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()  # loads the .env file automatically

app = Flask(__name__)

IBM_API_KEY    = os.environ.get("IBM_API_KEY")
IBM_PROJECT_ID = os.environ.get("IBM_PROJECT_ID")
IBM_URL        = os.environ.get("IBM_URL", "https://us-south.ml.cloud.ibm.com")

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=IBM_PROJECT_ID,
    params={
        "max_new_tokens": 800,
        "temperature": 0.7,
    }
)

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():
    data = request.get_json()
    topic  = data.get("topic", "").strip()
    domain = data.get("domain", "General").strip()

    if not topic:
        return jsonify({"error": "Please enter a research topic."}), 400

    prompt = f"""You are an expert academic research assistant.
Domain: {domain}
Research Topic: {topic}

Provide a well-structured research overview with:
1. Summary (3-4 sentences explaining the topic clearly)
2. Key Concepts (5 important concepts as bullet points)
3. Research Directions (3 areas worth exploring)
4. Suggested References (3 realistic academic paper titles with plausible authors)

Be concise, accurate, and academic in tone."""

    try:
        response = model.generate_text(prompt=prompt)
        return jsonify({"result": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
