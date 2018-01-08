{
  "targets": [
    {
      "target_name": "python3",
      "sources": [
        "src/python3.cc",
        "src/utils.cc",
        "src/py_object_wrapper.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
            "xcode_settings": {
              "OTHER_CFLAGS": [
                "-Wno-error=unused-command-line-argument",
                "<!(/usr/bin/python3-config --cflags)"
              ],
              "OTHER_LDFLAGS": [
                "<!(/usr/bin/python3-config --ldflags)"
              ]
            }
          }, { # not OSX
           "cflags": [ 
	          "-std=c++11",
             "<!(python3-config --cflags)"
          ],
          "libraries": [
             "<!(python3-config --libs)"
          ]
        }]
      ]
    }
  ]
}
