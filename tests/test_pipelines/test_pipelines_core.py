from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from creevey import CustomReportingPipeline
from creevey.load_funcs.image import load_image_from_url
from creevey.ops.image import record_mean_brightness
from creevey.write_funcs.image import write_image
from tests.conftest import (
    delete_file_if_exists,
    IMAGE_FILENAMES,
    IMAGE_URLS,
    keep_filename_save_png_in_tempdir,
    TEMP_DATA_DIR,
)


@pytest.fixture(scope='session')
def record_mean_brightness_pipeline():
    for url in IMAGE_URLS:
        outpath = keep_filename_save_png_in_tempdir(url)
        delete_file_if_exists(outpath)

    record_mean_brightness_pipeline = CustomReportingPipeline(
        load_func=load_image_from_url,
        ops=record_mean_brightness,
        write_func=write_image,
    )
    yield record_mean_brightness_pipeline
    for url in IMAGE_URLS:
        outpath = keep_filename_save_png_in_tempdir(url)
        delete_file_if_exists(outpath)


def test_custom_reporting_pipeline(record_mean_brightness_pipeline):
    inpaths = IMAGE_URLS
    outpaths = [
        TEMP_DATA_DIR / Path(filename).with_suffix('.png')
        for filename in IMAGE_FILENAMES
    ]
    exception_handled = skipped_existing = [0] * len(inpaths)
    expected_run_report = pd.DataFrame(
        {
            'outpath': outpaths,
            'skipped_existing': skipped_existing,
            'exception_handled': exception_handled,
        },
        index=inpaths,
    )
    actual_run_report = record_mean_brightness_pipeline.run(
        inpaths=inpaths,
        path_func=keep_filename_save_png_in_tempdir,
        n_jobs=6,
        skip_existing=False,
    )
    pd.testing.assert_frame_equal(
        actual_run_report.sort_index().drop(
            ['time_finished', 'mean_brightness'], axis='columns'
        ),
        expected_run_report.sort_index(),
    )
    assert np.issubdtype(actual_run_report.loc[:, 'mean_brightness'], np.number)
