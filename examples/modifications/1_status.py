#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""

import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(enable_camera_feed=True) as robot:
        battery_state = robot.get_battery_state()
        if battery_state:
            print("Robot battery voltage: {0}".format(battery_state.battery_volts))
            print("Robot battery Level: {0}".format(battery_state.battery_level))
            print("Robot battery is charging: {0}".format(battery_state.is_charging))
            print("Robot is on charger platform: {0}".format(battery_state.is_on_charger_platform))
            print("Robot's suggested charger time: {0}".format(battery_state.suggested_charger_sec))
        image = robot.camera.latest_image
        image.show()


if __name__ == "__main__":
    main()
