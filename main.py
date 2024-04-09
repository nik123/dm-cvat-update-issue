import os
import shutil

import datumaro as dm


def main():
    ds1 = dm.Dataset.import_from("dataset1", "cvat")
    print(f"Size of ds1: {len(ds1)}")

    ds2 = dm.Dataset.import_from("dataset2", "cvat")
    print(f"Size of ds2: {len(ds2)}")

    ds3 = ds1.update(ds2)
    print(f"Size of ds3 (before export): {len(ds3)}")

    # TODO: uncomment to keep the correct len of dataset
    # If exporting to cvat format, then id attribute inside 'image' tag
    # might be broken: id values are in random order and not unique.
    # Fixing it manually:
    # for idx, item in enumerate(ds3):
    #     item.attributes["frame"] = idx

    if os.path.exists("dataset3"):
        # Rm data for clean experiment
        shutil.rmtree("dataset3")
    ds3.export("dataset3", "cvat", save_media=True)

    # Import dataset again:
    ds3 = dm.Dataset.import_from("dataset3", "cvat")
    print(f"Size of ds3 (after import): {len(ds3)}")


if __name__ == "__main__":
    main()
