from pathlib import Path
import cv2


def annotate_images(
    input_img_paths: list[Path],
    output_path: Path,
    labels: list[str],
    max_size_display: int = 640,
) -> None:
    """Annotate images with class labels."""

    for img_path in input_img_paths:
        img = cv2.imread(str(img_path))

        # Resize Image
        ratio = max_size_display / max(img.shape[:2])
        img = cv2.resize(img, None, fx=ratio, fy=ratio)

        # add label help text
        for i, label in enumerate(labels):
            cv2.putText(
                img,
                f"{i}: {label}",
                (10, 30 + 30 * i),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

        # mapping from key to label
        labels_key_dict = {ord(str(i)): label for i, label in enumerate(labels)}

        # create all classification folders
        for label in labels:
            label_dir = output_path / label
            label_dir.mkdir(parents=True, exist_ok=True)

        cv2.imshow("Image", img)

        while True:
            key = cv2.waitKey(0)

            # Quit Annotation Tool
            if key == ord("q"):
                return

            if key in labels_key_dict:
                label = labels_key_dict[key]
                print(f"Classified as {label}")

                output_img_path = output_path / label / img_path.name
                img_path.rename(output_img_path)

                break

    cv2.destroyAllWindows()


def main():
    input_path = Path("input")
    input_img_paths = sorted(input_path.glob("*.jpg"))

    output_path = Path("output")
    output_path.mkdir(parents=True, exist_ok=True)

    annotate_images(
        input_img_paths=input_img_paths,
        output_path=output_path,
        labels=["usb_a", "usb_c", "usb_mini", "usb_micro"],
    )


if __name__ == "__main__":
    main()
