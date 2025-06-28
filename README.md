**FPGA-Based Edge Detection Using 2D Convolution**

This project implements a real-time edge detection system using the Sobel operator on the PYNQ-Z2 FPGA board. It leverages Vitis HLS, Vivado,
and the PYNQ framework to perform efficient hardware-software co-design, achieving high-speed and low-latency image processing suitable for applications such as ADAS, 
surveillance, and medical imaging.

**Abstract**

Edge detection is a fundamental step in many image processing and computer vi-
sion applications, enabling the identification of object boundaries and significant features
within an image. The present work involves the design and implementation of an edge
detection system using hardware acceleration techniques to achieve high performance and
low latency. The system processes input images by converting them to grayscale, ap-
plying a 2D convolution operation with an edge detection kernel, and generating output
images that highlight prominent edges. The filtering operation is implemented entirely in
hardware to optimize speed and efficiency, while the design is synthesized and dumped
onto the target hardware for execution. The system is validated through simulation and
experimental testing, demonstrating a substantial improvement in processing speed com-
pared to a purely software-based implementation. This work highlights the effectiveness
of hardware-based acceleration in enabling efficient image processing suitable for applica-
tions such as autonomous systems, surveillance, and medical imaging

**Objectives**

1. To implement edge detection using FPGA-based 2D convolution.
2. To utilize FPGA’s parallelism for fast and efficient image processing.
3. To evaluate the system’s performance in terms of speed and accuracy.


**Tools and Technologies**

| Category              | Tools / Platforms                       |
| --------------------- | --------------------------------------- |
| FPGA Platform         | Xilinx PYNQ-Z2 (Zynq-7000 SoC)          |
| Hardware Design       | Vivado, Vitis HLS                       |
| Software Interface    | Python, Jupyter Notebook, PYNQ APIs     |
| Programming Languages | C++, Python                             |
| Image Processing      | Sobel Operator, AXI DMA, 2D Convolution |




**System Architecture**

This project implements a fully hardware-based edge detection pipeline executed on the programmable logic (PL) of the PYNQ-Z2 FPGA. The processing is performed entirely in hardware, eliminating software-side computation of the Sobel operator.

**Hardware (PL - FPGA Fabric)**

->A custom-designed Sobel IP core developed using Vitis HLS

->Image data is streamed to the IP via AXI-Stream using DMA

->The 3×3 Sobel convolution is applied directly on the FPGA

->Gradient outputs are combined and thresholded within the FPGA

->Final edge-detected image is written back to memory and retrieved by the Python host for visualization and storage

**Software (PS - ARM Cortex-A9)**

->Only performs image loading and output handling

->Initiates hardware execution and controls data transfer via PYNQ API

->Displays and saves the processed output using Python libraries (e.g., PIL, matplotlib)



**Functional Workflow**

->Convert RGB image to grayscale.

->Transfer image to FPGA using AXI-DMA.

->Apply Sobel filter in hardware.

->Calculate gradient magnitude.

->Apply thresholding.

->Return the edge-detected image.


**Results**

The following table summarizes the FPGA resource utilization and performance metrics of the Sobel edge detection implementation:

| Metric                | Value                                   |
| --------------------- | --------------------------------------- |
|  LUTs Used            | 1374                                    |
| Flip-Flops            |  580                                    |
|  BRAM Blocks          | 3                                       |
| DSP Blocks            | 3                                       |
|  Latency              |  ~2,000,000 clock cycles                |



**Repository Structure**

* `.gitattributes` – Git attributes configuration
* `README.md` – Project overview and documentation
* `edge_detection.py` – Python script to interface with the FPGA using PYNQ
* `hls_sobel_axi_stream.cpp` – HLS top function: Sobel filter implementation
* `hls_sobel_axi_stream.hpp` – Header file for the HLS function
* `hls_sobel_axi_stream_tb.cpp` – C++ testbench for simulating the HLS design
* `input.jpg` – Sample input image for edge detection
* `output.jpg` – Output image after FPGA-based Sobel filtering





**Key Features**

->Real-time edge detection using hardware acceleration

->Efficient Sobel filter implementation using HLS

->Low resource usage with accurate edge detection

->Seamless integration with Jupyter Notebook on PYNQ

->Suitable for embedded vision applications



**Applications**

->ADAS (Advanced Driver Assistance Systems): Lane detection

->Surveillance: Motion and boundary detection

->Medical Imaging: Feature and tissue boundary extraction

->Robotics and Smart Agriculture: Visual perception



**Future Enhancements**

->Add Canny edge detection for improved edge quality

->Apply pipelining and loop unrolling in HLS

->Support real-time video stream or live camera input

->Integrate with CNN-based detectors

->Optimize for higher resolution image processing




**Authors**

Nidhi Desai 

Devika Vijapur 

Aishwarya Naik

Smita Ganur 

Under the guidance of **Prof. Supriya K**







