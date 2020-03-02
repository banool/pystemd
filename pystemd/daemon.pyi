# Copyright (c) 2020-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree.
#

from typing import AnyStr, Union

def notify(
    unset_environment: bool, *args: AnyStr, **kwargs: Union[int, str]
) -> None: ...
def listen_fds(a: bool) -> int: ...

LISTEN_FDS_START: int