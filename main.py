from pathlib import Path
import cv2


def annotate_images(
    input_img_paths: list[Path],
    output_path: Path,
    max_size_display: int = 640,
) -> None:
    """Annotate images with class labels."""

    for img_path in input_img_paths:
        img_original = cv2.imread(str(img_path))

        # Resize Image
        ratio = max_size_display / max(img_original.shape[:2])
        img = cv2.resize(img_original, None, fx=ratio, fy=ratio)

        while True:
            cv2.imshow("Image", img)

            key = cv2.waitKey(1) & 0xFF

            # Skip Image
            if key == ord(" "):
                break

            # Quit Annotation Tool
            if key == ord("q"):
                return
    
    cv2.destroyAllWindows()


def main():
    input_path = Path("input")
    input_img_paths = sorted(input_path.glob("*.jpg"))

    output_path = Path("output")
    output_path.mkdir(parents=True, exist_ok=True)

    annotate_images(input_img_paths, output_path)


if __name__ == "__main__":
    main()
