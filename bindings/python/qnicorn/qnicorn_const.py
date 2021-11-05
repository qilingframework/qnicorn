# For Qnicorn Engine. AUTO-GENERATED FILE, DO NOT EDIT [qnicorn_const.py]
QC_API_MAJOR = 1

QC_API_MINOR = 0
QC_VERSION_MAJOR = 1

QC_VERSION_MINOR = 0

QC_VERSION_EXTRA = 0
QC_SECOND_SCALE = 1000000
QC_MILISECOND_SCALE = 1000
QC_ARCH_ARM = 1
QC_ARCH_ARM64 = 2
QC_ARCH_MIPS = 3
QC_ARCH_X86 = 4
QC_ARCH_PPC = 5
QC_ARCH_SPARC = 6
QC_ARCH_M68K = 7
QC_ARCH_RISCV = 8
QC_ARCH_MAX = 9

QC_MODE_LITTLE_ENDIAN = 0
QC_MODE_BIG_ENDIAN = 1073741824

QC_MODE_ARM = 0
QC_MODE_THUMB = 16
QC_MODE_MCLASS = 32
QC_MODE_V8 = 64
QC_MODE_ARM926 = 128
QC_MODE_ARM946 = 256
QC_MODE_ARM1176 = 512
QC_MODE_MICRO = 16
QC_MODE_MIPS3 = 32
QC_MODE_MIPS32R6 = 64
QC_MODE_MIPS32 = 4
QC_MODE_MIPS64 = 8
QC_MODE_16 = 2
QC_MODE_32 = 4
QC_MODE_64 = 8
QC_MODE_PPC32 = 4
QC_MODE_PPC64 = 8
QC_MODE_QPX = 16
QC_MODE_SPARC32 = 4
QC_MODE_SPARC64 = 8
QC_MODE_V9 = 16
QC_MODE_RISCV32 = 4
QC_MODE_RISCV64 = 8

QC_ERR_OK = 0
QC_ERR_NOMEM = 1
QC_ERR_ARCH = 2
QC_ERR_HANDLE = 3
QC_ERR_MODE = 4
QC_ERR_VERSION = 5
QC_ERR_READ_UNMAPPED = 6
QC_ERR_WRITE_UNMAPPED = 7
QC_ERR_FETCH_UNMAPPED = 8
QC_ERR_HOOK = 9
QC_ERR_INSN_INVALID = 10
QC_ERR_MAP = 11
QC_ERR_WRITE_PROT = 12
QC_ERR_READ_PROT = 13
QC_ERR_FETCH_PROT = 14
QC_ERR_ARG = 15
QC_ERR_READ_UNALIGNED = 16
QC_ERR_WRITE_UNALIGNED = 17
QC_ERR_FETCH_UNALIGNED = 18
QC_ERR_HOOK_EXIST = 19
QC_ERR_RESOURCE = 20
QC_ERR_EXCEPTION = 21
QC_MEM_READ = 16
QC_MEM_WRITE = 17
QC_MEM_FETCH = 18
QC_MEM_READ_UNMAPPED = 19
QC_MEM_WRITE_UNMAPPED = 20
QC_MEM_FETCH_UNMAPPED = 21
QC_MEM_WRITE_PROT = 22
QC_MEM_READ_PROT = 23
QC_MEM_FETCH_PROT = 24
QC_MEM_READ_AFTER = 25

QC_TCG_OP_SUB = 0
QC_TCG_OP_FLAG_CMP = 1
QC_TCG_OP_FLAG_DIRECT = 2
QC_HOOK_INTR = 1
QC_HOOK_INSN = 2
QC_HOOK_CODE = 4
QC_HOOK_BLOCK = 8
QC_HOOK_MEM_READ_UNMAPPED = 16
QC_HOOK_MEM_WRITE_UNMAPPED = 32
QC_HOOK_MEM_FETCH_UNMAPPED = 64
QC_HOOK_MEM_READ_PROT = 128
QC_HOOK_MEM_WRITE_PROT = 256
QC_HOOK_MEM_FETCH_PROT = 512
QC_HOOK_MEM_READ = 1024
QC_HOOK_MEM_WRITE = 2048
QC_HOOK_MEM_FETCH = 4096
QC_HOOK_MEM_READ_AFTER = 8192
QC_HOOK_INSN_INVALID = 16384
QC_HOOK_EDGE_GENERATED = 32768
QC_HOOK_TCG_OPCODE = 65536
QC_HOOK_MEM_UNMAPPED = 112
QC_HOOK_MEM_PROT = 896
QC_HOOK_MEM_READ_INVALID = 144
QC_HOOK_MEM_WRITE_INVALID = 288
QC_HOOK_MEM_FETCH_INVALID = 576
QC_HOOK_MEM_INVALID = 1008
QC_HOOK_MEM_VALID = 7168
QC_QUERY_MODE = 1
QC_QUERY_PAGE_SIZE = 2
QC_QUERY_ARCH = 3
QC_QUERY_TIMEOUT = 4

QC_CTL_IO_NONE = 0
QC_CTL_IO_WRITE = 1
QC_CTL_IO_READ = 2
QC_CTL_IO_READ_WRITE = 3

QC_CTL_QC_MODE = 0
QC_CTL_QC_PAGE_SIZE = 1
QC_CTL_QC_ARCH = 2
QC_CTL_QC_TIMEOUT = 3
QC_CTL_QC_USE_EXITS = 4
QC_CTL_QC_EXITS_CNT = 5
QC_CTL_QC_EXITS = 6
QC_CTL_CPU_MODEL = 7
QC_CTL_TB_REQUEST_CACHE = 8
QC_CTL_TB_REMOVE_CACHE = 9

QC_PROT_NONE = 0
QC_PROT_READ = 1
QC_PROT_WRITE = 2
QC_PROT_EXEC = 4
QC_PROT_ALL = 7
