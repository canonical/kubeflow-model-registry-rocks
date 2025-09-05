# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.
import pytest
import subprocess

from charmed_kubeflow_chisme.rock import CheckRock


@pytest.mark.abort_on_fail
def test_rock():
    """Test rock."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    # assert the rock contains the expected files
    for image_subdir_path in ["/mr-storage-initializer"]:
        subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "--entrypoint",
                "/bin/bash",
                LOCAL_ROCK_IMAGE,
                "-c",
                f"ls -la {image_subdir_path}",
            ],
            check=True,
        )
