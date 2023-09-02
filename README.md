# Raspberry-Security-Camera

## Overview

This repository provides a simple, efficient, and resource-light solution to set up a motion-detection security camera using a Raspberry Pi. The Python script utilizes OpenCV for video capture and motion detection.

## Prerequisites

1. A Raspberry Pi with Raspbian OS installed.
2. A camera module compatible with Raspberry Pi.
3. Python 3.x installed on the Raspberry Pi.

## Dependencies

The script uses the following Python libraries:
- OpenCV
- NumPy

You can install these using the following commands:

```bash
sudo apt-get update
sudo apt-get install python3-opencv
```

## Installation

1. Clone this repository to your Raspberry Pi.
2. Update the `save_path` variable in the `SecurityCam.py` script with the path where you'd like to save the captured images.

## Running the Script

To run the script manually, navigate to the repository folder and execute:

```bash
python3 SecurityCam.py
```

Press `q` to stop the script.

## Auto-Start on Boot

To have the script run automatically in the background upon Raspberry Pi startup, you can set up a `systemd` service.

### Create a systemd Service File

1. Open a new file in the `/etc/systemd/system/` directory:

    ```bash
    sudo nano /etc/systemd/system/motion_camera.service
    ```

2. Add the following content:

    ```ini
    [Unit]
    Description=Motion Camera Service
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /path/to/your/SecurityCam.py
    WorkingDirectory=/path/to/your/
    StandardOutput=inherit
    StandardError=inherit
    Restart=always
    User=pi

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `/path/to/your/SecurityCam.py` with the full path to your Python script and `/path/to/your/` with the directory where the script resides.

### Enable and Start the Service

3. Reload the `systemd` daemon and enable the service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable motion_camera.service
    ```

4. Start the service:

    ```bash
    sudo systemctl start motion_camera.service
    ```

### Service Management

- To check the service status: `sudo systemctl status motion_camera.service`
- To stop the service: `sudo systemctl stop motion_camera.service`
- To restart the service: `sudo systemctl restart motion_camera.service`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Feel free to contribute to this project. For any issues or feature requests, please open an issue or submit a pull request.