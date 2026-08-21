import ollama
#config
MODEL = "qwen2.5:3b"
#agent1: writer

WRITER_SYSTEM_PROMPT = """
You are Agent 1, a professional research writer.

Your responsibility is to create a first draft about the
topic provided by the user.

Your draft should:
- Explain the topic clearly.
- Use a logical structure.
- Include useful and relevant information.
- Be easy for a general audience to understand.
- Avoid unnecessary repetition.
- Avoid making unsupported claims.
- Use headings when useful.

You are the WRITER only.
Do not discuss the editing process.
"""

#agent2:editor/critic

EDITOR_SYSTEM_PROMPT = """
You are Agent 2, an expert editor and critic.

You will receive a topic and a draft created by another AI
agent.

Your responsibilities are to:

1. Check the draft for clarity.
2. Check the organization and structure.
3. Remove unnecessary repetition.
4. Identify vague or unsupported claims.
5. Improve explanations.
6. Correct obvious factual problems.
7. Add important information that is missing.
8. Make the final response concise but informative.

Do not simply rewrite the draft.

Make meaningful improvements while preserving useful
information from the original.

Return ONLY the improved final article.
"""


#calling an Ollama agent
def run_agent(system_prompt, user_prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response["message"]["content"]

#multi agent pipeline
def run_pipeline(topic):

    print("\n" + "=" * 70)
    print(f"TOPIC: {topic}")
    print("=" * 70)

    # Agent 1

    print("\n[Agent 1: Writer] Creating draft...\n")

    draft = run_agent(
        WRITER_SYSTEM_PROMPT,
        f"""
Write a first draft about:

{topic}
"""
    )

    print("-" * 70)
    print("AGENT 1 - RAW DRAFT")
    print("-" * 70)
    print(draft)

    # Agent 2

    print("\n[Agent 2: Editor] Reviewing draft...\n")

    editor_input = f"""
Topic:
{topic}

Here is the draft produced by Agent 1:

---------------- BEGIN WRITER DRAFT ----------------

{draft}

----------------- END WRITER DRAFT -----------------

Review the Writer's draft and produce an improved final
version.
"""

    final_output = run_agent(
        EDITOR_SYSTEM_PROMPT,
        editor_input
    )

    print("-" * 70)
    print("AGENT 2 - FINAL EDITED OUTPUT")
    print("-" * 70)
    print(final_output)

    return draft, final_output

#experiment on TWO topics
topics = [
    "How generative AI is changing education",
    "Benefits and risks of artificial intelligence in healthcare"
]


for topic in topics:

    draft, final = run_pipeline(topic)

    print("\n\n")
