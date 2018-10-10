
getDevices(template1) {
    return new Promise((resolve, reject) => {
      logger.debug("im here 22222");
      const devicesFound = [];
      function getDevicesList(page, template) {
        axios.get(config.deviceManager.url + "/device/template/" + template +
          "?page_size=1&page_num=" + page,
          {
            'headers': { 'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJoUWEwaW1UdWI5TG1wMlpKalBVdVZrQlNEd0oyS0pzYiIsImlhdCI6MTUzMzkwNTk4MiwiZXhwIjoxNTMzOTA2NDAyLCJuYW1lIjoiQWRtaW4gKHN1cGVydXNlcikiLCJlbWFpbCI6ImFkbWluQG5vZW1haWwuY29tIiwicHJvZmlsZSI6ImFkbWluIiwiZ3JvdXBzIjpbMV0sInVzZXJpZCI6MSwianRpIjoiZmMwZGY5ZTU0OGQyYjZhMTM4N2EzY2Y5ZTFhNWQxYTYiLCJzZXJ2aWNlIjoiYWRtaW4iLCJ1c2VybmFtZSI6ImFkbWluIn0.39koot0phx9QT4At5nsDgK_xbc6gQfsqJ7oyHNtrYX8" }
          }).then((response) => {
            if (response.data.devices.length === 0) {
              resolve(devicesFound);
            }
            response.data.devices.forEach((device) => {
              if (device.hasOwnProperty('id')) {
                devicesFound.push(device.id);
              }
            })
            if (response.data.pagination.has_next) {
              getDevicesList(response.data.pagination.next_page, template);
            } else {
              resolve(devicesFound);
              return;
            }
          }).catch((error) => {
            reject(error);
            return;
          });
      }
      getDevicesList(1, template1);

    });
  }