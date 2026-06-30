import re

EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_REGEX = re.compile(
    r"(\+?\d[\d\s\-\(\)]{8,}\d)"
)

KNOWN_SKILLS = {
    "python",
    "java",
    "c++",
    "sql",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "react",
    "node.js",
    "typescript",
    "javascript",
    "fastapi",
    "flask",
    "django",
    "spring",
    "spring boot",
    "redis",
    "kafka",
    "mongodb",
    "mysql",
    "postgresql",
    "machine learning",
    "tensorflow",
    "pytorch",
    "opencv",
    "git",
    "linux"
}

KNOWN_DEGREES = [
    "B.Tech",
    "M.Tech",
    "B.E",
    "M.E",
    "Bachelor",
    "Master",
    "MBA",
    "PhD"
]