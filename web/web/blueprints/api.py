#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Blueprint, abort, jsonify, g
import json

import grpc
from google.protobuf.empty_pb2 import Empty

from collector_pb2_grpc import DataCollectorStub

api = Blueprint("api", __name__)

host = os.getenv("COLLHOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50051")
client = DataCollectorStub(channel)

@api.route("/collect")
def collect():
    data = []
    response = client.Collect(Empty())
    for state in response.states:
        data.append({"time": state.step.ToDatetime(), "meter": state.meter})
    return jsonify(data)
