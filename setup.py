import platform

from setuptools import Extension, setup


def get_ext_modules() -> list:
    """
    获取三方模块

    Mac由于缺乏二进制库支持无法使用
    """

    if platform.system() == "Linux":
        extra_compile_flags = [
            "-std=c++17",
            "-O3",
            "-Wno-delete-incomplete",
            "-Wno-sign-compare",
        ]
        extra_link_args = ["-lstdc++"]
        runtime_library_dirs = ["$ORIGIN"]
    else:
        extra_compile_flags = ["-O2", "-MT"]
        extra_link_args = []
        runtime_library_dirs = []

    vnctpmd = Extension(
        name="vcat_ctp.api.vnctpmd",
        sources=["vcat_ctp/api/vnctp/vnctpmd/vnctpmd.cpp"],
        include_dirs=["vcat_ctp/api/include", "vcat_ctp/api/vnctp"],
        library_dirs=["vcat_ctp/api/libs", "vcat_ctp/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=extra_compile_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        language="cpp",
    )

    vnctptd = Extension(
        name="vcat_ctp.api.vnctptd",
        sources=["vcat_ctp/api/vnctp/vnctptd/vnctptd.cpp"],
        include_dirs=["vcat_ctp/api/include", "vcat_ctp/api/vnctp"],
        library_dirs=["vcat_ctp/api/libs", "vcat_ctp/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=extra_compile_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        language="cpp",
    )

    return [vnctptd, vnctpmd]

    
setup(ext_modules=get_ext_modules())
