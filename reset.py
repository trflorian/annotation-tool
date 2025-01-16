from pathlib import Path

def main():
    input_path = Path("input")
    input_path.mkdir(parents=True, exist_ok=True)

    output_path = Path("output")

    if not output_path.exists():
        return

    annotated_images = output_path.glob("*/*.jpg")

    # move annotated images back to input folder
    for img_path in annotated_images:
        img_path.rename(input_path / img_path.name)


if __name__ == "__main__":
    main()
