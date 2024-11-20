# Copyright (c) 2024 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Allen Robel"

import logging

from ..config import Config


class Federation(Config):
    """
    ## Federation API enpoints - Api().Config().Federation()

    ### Description
    Common methods and properties for API Federation subclasses.

    ### Path
    ``/api/config/federation/``
    """

    def __init__(self):
        super().__init__()
        self.class_name = self.__class__.__name__
        self.log = logging.getLogger(f"dcnm.{self.class_name}")
        self.log.debug("ENTERED api.config.Federation()")
        self.federation = f"{self.config}/federation"


class EpFederationMembers(Federation):
    def __init__(self):
        super().__init__()
        self.class_name = self.__class__.__name__
        self.log = logging.getLogger(f"dcnm.{self.class_name}")

        self._verb = "GET"
        self._path = f"{self.federation}/members"
        msg = "ENTERED api.config.federation."
        msg += f"Federation.{self.class_name}"
        self.log.debug(msg)