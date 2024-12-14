## Arch Paper List
A list of classic and recent papers for Computer Architecture research.

(especially traditional research on processors, topics like GPGPU, DSA and PIM are not covered here)

### 1. Classic Paper

> Recommended from Advanced Computer Architecture course.

- [1] Architecture of the IBM System/360, 1964
    - First proposal of the ISA concept
- [2] Parallel operation in the control data 6600, 1964
    - First supercomputer in the world
- [3] An Efficient Algorithm for Exploiting Multiple Arithmetic Units, 1967
    - The famous Tomasulo Algorithm
- [4] The case for the reduced instruction set computer, 1980
    - The emerging of RISC processors
- [5] Very Long Instruction Word architectures and the ELI-512, 1983
- [6] Using cache memory to reduce processor-memory traffic, 1983
- [7] Decoupled access/execute computer architectures, 1984
- [8] A VLIW architecture for a trace scheduling compiler, 1988
- [9] The MIPS M2000 system, 1988
- [10] The Tera computer system, 1990
- [11] Improving direct-mapped cache performance by the addition of a small fully-associative cache and prefetch buffers, 1990
- [12] Combining Branch Predictors, 1993
- [13] A comparison of dynamic branch predictors that use two levels of branch history, 1993
- [14] Maximizing On-Chip Parallelism, 1995
- [15] Shared memory consistency models: a tutorial, 1996
- [16] Exploiting Choice: Instruction Fetch and Issue on an Implementable Simultaneous Multithreading Processor, 1996
- [17] The MIPS R10000 superscalar microprocessor, 1996
    - Must-read paper for processor design
- [18] Lockup-free instruction fetch/prefetch cache organization, 1998
- [19] The Alpha 21264 microprocessor, 1999
    - Must-read paper for processor design
- [20] A PPM-like, tag-based branch predictor, 2005
- [21] A case for (partially) TAgged GEometric history length branch prediction, 2006
    - Widely adopted in modern processors

### 2. Microarchitecture

> Computer Architecture = ISA + Microarchitecture.

- [22] Processor Microarchitecture An Implementation Perspective, 2011
    - Synthesis Lectures on Computer Architecture

#### 2.1. Branch
- [23] Branch Target Buffer Organizations, 2023, MICRO
- [24] AVM-BTB: Adaptive and Vritualized Multi-level Branch Target Buffer, 2024, ISCA

#### 2.2. Rename
- [25] STRAIGHT: Hazardless Processor Architecture Without Register Renaming, 2018, MICRO
- [26] Clockhands: Rename-free Instruction Set Architecture for Out-of-order Processors, 2023, MICRO
- [27] Speculative Register Reclamation, 2023, HPCA

#### 2.3. Schedule
- [28] CASINO Core Microarchitecture: Generating Out-of-Order Schedules Using Cascaded In-Order Scheduling Windows, 2020, HPCA
- [29] Reconstructing Out-of-Order Issue Queue, 2022, MICRO
- [30] CRISP: critical slice prefetching, 2022, ASPLOS
- [31] Orinoco: Ordered Issue and Unordered Commit with Non-Collapsible Queues, 2023, ISCA

#### 2.4. Load/Store Unit
- [32] Reducing design complexity of the load/store queue, 2003, MICRO
- [33] Effective Context-Sensitive Memory Dependence Prediction, 2024, HPCA

#### 2.4. Others
- [34] Vector Runhead, 2021, ISCA
- [35] Register file prefetching, 2022, ISCA
- [36] Decoupled Vector Runhead, 2023, MICRO
- [37] Simultaneous and Heterogenous Multithreading, 2023, MICRO

#### 2.5 Processors
- [38] The Rocket Chip Generator, 2016
- [39] Inside 6th-generation Intel core: New microarchitecture codenamed Skylake, 2017, IEEE Micro
- [40] Xuantie-910: A Commercial Multi-Core 12-Stage Pipeline Out-of-Order 64-bit High Performance RISC-V Processor with Vector Extension, 2020, ISCA
- [41] SonicBOOM: The 3rd Generation Berkeley Out-of-Order Machine, 2020
- [42] "Zen 4": The AMD 5nm 5.7GHz x86-64 Microprocessor Core, 2023, ISSCC

### 3. Memory System

#### 3.1. Cache
- [43] Spatial Memory Streaming, 2006, ISCA
- [44] Bypass and Insertion Algorithms for Exclusive Last-level Caches, 2011, ISCA
- [45] Bingo Spatial Data Prefetcher, 2019, HPCA
- [46] Classifying Memory Access Patterns for Prefetching, 2020, ASPLOS
- [47] Bouquet of Instruction Pointers: Instruction Pointer Classifier-based Spatial Hardware Prefetching, 2020, ISCA
- [48] Pythia: A Customizable Hardware Prefetching Framework Using Online Reinforcement Learning, 2021, MICRO
- [49] Hermes: Accelerating Long-Latency Load Requests via Perceptron-Based Off-Chip Load Prediction, 2022, MICRO
- [50] Berti: an Accurate Local-Delta Data Prefetcher, 2022, MICRO
- [51] Reducing Load Latency with Cache Level Prediction, 2022, HPCA
- [52] CLIP: Load Criticality based Data Prefetching for Bandwidth-constrained Many-core Systems, 2023, MICRO
- [53] EMISSARY: Enhanced Miss Awareness Replacement Policy for L2 Instruction Caching, 2023, ISCA
- [54] Compression-Aware and Performance-Efficient Insertion Policies for Long-Lasting Hybrid LLCs, 2023, HPCA
- [55] Differential-Matching Prefetcher for Indirect Memory Access, 2024, HPCA

#### 3.2. MMU
- [56] Mosaic Pages: Big TLB Reach with Small Pages, 2023, ASPLOS
- [57] Victima: Drastically Increasing Address Translation Reach by Leveraging Underutilized Cache Resources, 2023, MICRO
- [58] Memory-Efficient Hashed Page Tables, 2023, HPCA
- [59] Contiguitas: The Pursuit of Physical Memory Contiguity in Datacenters, 2023, ISCA

#### 3.3. DRAM
- [60] NOMAD: Enabling Non-blocking OS-managed DRAM Cache via Tag-Data Decoupling, 2023, HPCA

### 4. Design & Analysis

> Design and Analysis are two sides of the same coin.

#### 4.1. Platform & Tools
- [61] McPAT: An integrated power, area, and timing modeling framework for multicore and manycore architectures, 2009, MICRO
- [62] CACTI-P: Architecture-level modeling for srambased structures with advanced leakage reduction techniques, 2011, ICCAD
- [63] SPEC CPU2017 Benchmark Tools, 2017
- [64] Firesim: FPGA-Accelerated Cycle-Exact Scale-Out System Simulation in the Public Cloud, 2018, ISCA
- [65] Towards Developing High Performance RISC-V Processors Using Agile Methodology, 2022, MICRO

#### 4.2. RTL Simulation
- [66] Efficiently Exploiting Low Activity Factors to Accelerate RTL Simulation, 2020, DAC
- [67] RepCut: Superlinear Parallel RTL Simulation with Replication-Aided Partitioning, 2023, ASPLOS
- [68] Khronos: Fusing Memory Access for Improved Hardware RTL Simulation, 2023, MICRO
- [69] Don't Repeat Yourself! Course-Grained Circuit Deduplication to Accelerate RTL Simulation, 2024, ASPLOS

#### 4.3. Performance Analysis
- [70] Automatically Characterizing Large Scale Program Behavior, 2002, ASPLOS
- [71] A Top-Down method for performance analysis and counters architecture, 2014, ISPASS
- [72] TIP: Time-Proportional Instruction Profiling, 2021, MICRO
- [73] TEA: Time-Proportional Event Analysis, 2023, ISCA
- [74] MBAPIS: Multi-Level Behavior Analysis Guided Program Interval Selection for Microarchitecture Studies, 2023, PACT
- [75] ArchExplorer: Microarchitecture Exploration Via Bottleneck Analysis, 2023, MICRO

### 5. Survey
