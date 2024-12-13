## Arch Paper List
A list of classic and recent papers for Computer Architecture research.

(especially traditional research on processors, topics like GPGPU, DSA and PIM are not covered here)

### 1. Classic Paper
- [*] Architecture of the IBM System/360, 1964
    - (First proposal of the ISA concept)
- [*] Parallel operation in the control data 6600, 1964
- [*] An Efficient Algorithm for Exploiting Multiple Arithmetic Units, 1967
    - (The famous Tomasulo Algorithm)
- [*] The case for the reduced instruction set computer, 1980
    - (The emerging of RISC processors)
- [*] Very Long Instruction Word architectures and the ELI-512, 1983
- [*] Using cache memory to reduce processor-memory traffic, 1983
- [*] Decoupled access/execute computer architectures, 1984
- [*] A VLIW architecture for a trace scheduling compiler, 1988
- [*] The MIPS M2000 system, 1988
- [*] The Tera computer system, 1990
- [*] Improving direct-mapped cache performance by the addition of a small fully-associative cache and prefetch buffers, 1990
- [*] Combining Branch Predictors, 1993
- [*] A comparison of dynamic branch predictors that use two levels of branch history, 1993
- [*] Maximizing On-Chip Parallelism, 1995
- [*] Shared memory consistency models: a tutorial, 1996
- [*] Exploiting Choice: Instruction Fetch and Issue on an Implementable Simultaneous Multithreading Processor, 1996
- [*] The MIPS R10000 superscalar microprocessor, 1996
    - (Must-read paper for processor design)
- [*] Lockup-free instruction fetch/prefetch cache organization, 1998
- [*] The Alpha 21264 microprocessor, 1999
    - (Must-read paper for processor design)
- [*] A PPM-like, tag-based branch predictor, 2005
- [*] A case for (partially) TAgged GEometric history length branch prediction, 2006
    - (Widely adopted in modern processors)

(Recommanded from PKU's Advanced Computer Architecture Course)

### 2. Microarchitecture
- [*] Processor Microarchitecture An Implementation Perspective, 2011
    - (Synthesis Lectures on Computer Architecture)

#### 2.1. Branch
- [*] Branch Target Buffer Organizations, 2023, MICRO
- [*] AVM-BTB: Adaptive and Vritualized Multi-level Branch Target Buffer, 2024, ISCA

#### 2.2. Rename
- [*] STRAIGHT: Hazardless Processor Architecture Without Register Renaming, 2018, MICRO
- [*] Clockhands: Rename-free Instruction Set Architecture for Out-of-order Processors, 2023, MICRO
- [*] Speculative Register Reclamation, 2023, HPCA

#### 2.3. Schedule
- [*] CASINO Core Microarchitecture: Generating Out-of-Order Schedules Using Cascaded In-Order Scheduling Windows, 2020, HPCA
- [*] Reconstructing Out-of-Order Issue Queue, 2022, MICRO
- [*] CRISP: critical slice prefetching, 2022, ASPLOS
- [*] Orinoco: Ordered Issue and Unordered Commit with Non-Collapsible Queues, 2023, ISCA

#### 2.4. Load/Store Unit
- [*] Reducing design complexity of the load/store queue, 2003, MICRO
- [*] Effective Context-Sensitive Memory Dependence Prediction, 2024, HPCA

#### 2.4. Others
- [*] Vector Runhead, 2021, ISCA
- [*] Register file prefetching, 2022, ISCA
- [*] Decoupled Vector Runhead, 2023, MICRO
- [*] Simultaneous and Heterogenous Multithreading, 2023, MICRO

#### 2.5 Processors
- [*] The Rocket Chip Generator, 2016
- [*] Inside 6th-generation Intel core: New microarchitecture codenamed Skylake, 2017, IEEE Micro
- [*] Xuantie-910: A Commercial Multi-Core 12-Stage Pipeline Out-of-Order 64-bit High Performance RISC-V Processor with Vector Extension, 2020, ISCA
- [*] SonicBOOM: The 3rd Generation Berkeley Out-of-Order Machine, 2020
- [*] "Zen 4": The AMD 5nm 5.7GHz x86-64 Microprocessor Core, 2023, ISSCC

### 3. Memory System

#### 3.1. Cache

#### 3.2. MMU

#### 3.3. DRAM

### 4. Design and Analysis

#### 4.1. Platform
- [*] McPAT: An integrated power, area, and timing modeling framework for multicore and manycore architectures, 2009, MICRO
- [*] CACTI-P: Architecture-level modeling for srambased structures with advanced leakage reduction techniques, 2011, ICCAD
- [*] SPEC CPU2017 Benchmark Tools, 2017
- [*] Firesim: FPGA-Accelerated Cycle-Exact Scale-Out System Simulation in the Public Cloud, 2018, ISCA
- [*] Towards Developing High Performance RISC-V Processors Using Agile Methodology, 2022, MICRO

#### 4.2. RTL Simulation
- [*] Efficiently Exploiting Low Activity Factors to Accelerate RTL Simulation, 2020, DAC
- [*] RepCut: Superlinear Parallel RTL Simulation with Replication-Aided Partitioning, 2023, ASPLOS
- [*] Khronos: Fusing Memory Access for Improved Hardware RTL Simulation, 2023, MICRO
- [*] Don't Repeat Yourself! Course-Grained Circuit Deduplication to Accelerate RTL Simulation, 2024, ASPLOS

#### 4.3. Performance Analysis
- [*] Automatically Characterizing Large Scale Program Behavior, 2002, ASPLOS
- [*] A Top-Down method for performance analysis and counters architecture, 2014, ISPASS
- [*] TIP: Time-Proportional Instruction Profiling, 2021, MICRO
- [*] TEA: Time-Proportional Event Analysis, 2023, ISCA
- [*] MBAPIS: Multi-Level Behavior Analysis Guided Program Interval Selection for Microarchitecture Studies, 2023, PACT
- [*] ArchExplorer: Microarchitecture Exploration Via Bottleneck Analysis, 2023, MICRO

### 5. Survey