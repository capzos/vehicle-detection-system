"""Small Git helpers for Colab. The token comes from Colab Secrets and is never saved or printed."""
import base64
import subprocess


def _run(args, repo_dir, hide=()):
    """Run a git command, print its output with any secrets hidden, and return True if it worked."""
    result = subprocess.run(args, cwd=repo_dir, capture_output=True, text=True)
    output = result.stdout + result.stderr
    for secret in hide:
        if secret:
            output = output.replace(secret, "***")
    print(output.strip())
    return result.returncode == 0


def git_pull(repo_dir):
    """Get new commits from GitHub. The repo is public, so no token is needed.
    --ff-only means: only update if it's simple. Never make a surprise merge."""
    ok = _run(["git", "pull", "--ff-only"], repo_dir)
    print("✅ Pull OK" if ok else "❌ Pull FAILED - read the message above")
    return ok


def git_push(repo_dir, github_user, branch="main"):
    """Push to GitHub using the token from Colab Secrets, for this one command only."""
    from google.colab import userdata
    token = userdata.get("GITHUB_TOKEN")
    basic = base64.b64encode(f"{github_user}:{token}".encode()).decode()
    ok = _run(
        ["git", "-c", f"http.https://github.com/.extraheader=AUTHORIZATION: basic {basic}",
         "push", "origin", branch],
        repo_dir, hide=(token, basic),
    )
    print("✅ Push OK" if ok else "❌ Push FAILED - read the message above")
    return ok
