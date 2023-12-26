# tomzinha

## https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python
## https://vulkan.lunarg.com/doc/view/latest/linux/getting_started_ubuntu.html
------
### wget -qO- https://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo tee /etc/apt/trusted.gpg.d/lunarg.asc
### sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-jammy.list http://packages.lunarg.com/vulkan/lunarg-vulkan-jammy.list
### sudo apt update
### sudo apt install vulkan-sdk

### git clone --recurse-submodules https://github.com/nomic-ai/gpt4all.git
### cd gpt4all/gpt4all-backend/
### mkdir build
### cd build
### cmake ..
### cmake --build . --parallel  # optionally append: --config Release
### cd ../../gpt4all-bindings/python
### pip3 install -e .

## install VULKAN
### mkdir build
### cd build
### cmake ..
### make -j8
### ------------------------------
### wget -qO- https://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo tee /etc/apt/trusted.gpg.d/lunarg.asc
### sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-jammy.list http://packages.lunarg.com/vulkan/lunarg-vulkan-jammy.list
### sudo apt update
### sudo apt install vulkan-sdk