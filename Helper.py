def choose(title, options, back_label=None):
    """Show a numbered menu and return the chosen option (or None for back/quit)."""
    while True:
        print(f"\n=== {title} ===")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        print(f"  0. {back_label or 'Quit'}")

        raw = input("Select: ").strip()
        if raw == "0":
            return None
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print("Invalid choice, try again.")