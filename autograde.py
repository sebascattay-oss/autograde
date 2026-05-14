import argparse
from github import Github

def check_repo(repo_name):
    g = Github()  # No token needed for public repos
    try:
        repo = g.get_repo(repo_name)
    except Exception as e:
        print(f"❌ Error accessing repository: {e}")
        return False

    # 1. The project is a git repository
    # All GitHub repositories are git repositories
    print("✅ 1. The project is a git repository: Yes")

    # 2. That the "main" branch exists
    try:
        repo.get_branch("main")
        print("✅ 2. That the 'main' branch exists: Yes")
    except:
        print("❌ 2. That the 'main' branch exists: No")
        return False

    # 3. That the "feature" branch exists in remote
    try:
        repo.get_branch("feature")
        print("✅ 3. That the 'feature' branch exists in remote: Yes")
    except:
        print("❌ 3. That the 'feature' branch exists in remote: No")
        return False

    # 4. That the "file1.txt" file exists in main
    try:
        repo.get_contents("file1.txt", ref="main")
        print("✅ 4. That the 'file1.txt' file exists in main: Yes")
    except:
        print("❌ 4. That the 'file1.txt' file exists in main: No")
        return False

    return True

def main():
    parser = argparse.ArgumentParser(
        description="Inspect a GitHub repository and report if it meets specified conditions.",
        epilog="Examples:\n  autograde.py owner/repo\n  autograde.py (interactive mode)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("repo", nargs="?", help="GitHub repository in format 'owner/repo' (optional, will ask if not provided)")
    args = parser.parse_args()

    # If no repository provided, ask interactively
    if not args.repo:
        print("\n" + "="*60)
        print("🔍 AUTOGRADE - GitHub Repository Validator")
        print("="*60 + "\n")
        
        repo_input = input("📍 Enter the GitHub repository (format: owner/repo): ").strip()
        
        if not repo_input:
            print("❌ No repository provided. Exiting.")
            return
        
        args.repo = repo_input
    
    print("\n" + "="*60)
    print(f"📊 Checking repository: {args.repo}")
    print("="*60 + "\n")
    
    success = check_repo(args.repo)
    
    print("\n" + "="*60)
    if success:
        print("✅ All conditions met! Repository is valid.")
    else:
        print("❌ Some conditions not met. Repository is invalid.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()