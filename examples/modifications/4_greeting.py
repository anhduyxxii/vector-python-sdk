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
from datetime import datetime

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Greeting...")
        robot.say_text(f'Good {get_part_of_day()} Moc Ziap')
        print("Playing animation...")
        robot.anim.play_animation('anim_feedback_goodrobot_02')

def get_part_of_day():
  hour = datetime.now().hour
  return (
    "morning" if 5 <= hour <= 11
    else
    "afternoon" if 12 <= hour <= 17
    else
    "evening" if 18 <= hour <= 22
    else
    "night"
  )

if __name__ == "__main__":
    main()
