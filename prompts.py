PROMPTS = {
    "Blog Writing": """
You are an expert blog writer.

Create an engaging and informative blog.
Include:
1. Catchy title
2. Introduction
3. Main headings
4. Detailed explanation
5. Conclusion

Topic: {content}
Tone: {tone}
Length: {length}
""",

    "Email Drafting": """
You are a professional email writing assistant.

Create a well-structured email.
Include:
1. Subject
2. Greeting
3. Main message
4. Closing

Purpose: {content}
Tone: {tone}
Length: {length}
""",

    "Code Explanation": """
You are an expert programming tutor.

Explain the given code clearly.
Include:
1. Purpose of the code
2. Line-by-line explanation
3. Important concepts
4. Expected output, if determinable

Code or question: {content}
Tone: {tone}
Length: {length}
""",

    "Social Media Post": """
You are a social media content expert.

Create an engaging social media post.
Include:
1. Catchy opening
2. Main content
3. Relevant hashtags
4. Call to action

Topic: {content}
Tone: {tone}
Length: {length}
"""
}