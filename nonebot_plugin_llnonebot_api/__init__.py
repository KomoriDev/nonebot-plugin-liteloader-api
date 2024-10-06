import nonebot
from fastapi import FastAPI
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

from .router import router as api_router

__version__ = "0.1.0"

__plugin_meta__ = PluginMetadata(
    name="LiteLoader-NoneBot API",
    description="为 LLNoneBot 提供 API 服务",
    usage="配合 LiteLoader-NoneBot 使用",
    type="application",
    config=None,
    homepage="https://github.com/KomoriDev/nonebot-plugin-liteloader-api",
    supported_adapters=None,
    extra={
        "unique_name": "LiteLoader-NoneBot API",
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.0",
    },
)

__description__ = """
**A program that provide API services for [LLNoneBot](https://github.com/KomoriDev/LiteLoaderQQNT-NoneBot). 🚀**

Project:

  - LLNoneBot: [KomoriDev/LiteLoaderQQNT-NoneBot](https://github.com/KomoriDev/LiteLoaderQQNT-NoneBot)
  - LLNoneBot API: [KomoriDev/nonebot-plugin-llnonebot-api](https://github.com/KomoriDev/nonebot-plugin-llnonebot-api)
"""  # noqa: E501

driver = nonebot.get_driver()

api: FastAPI = FastAPI(
    debug=True if driver.config.log_level == "DEBUG" else False,
    title=__plugin_meta__.name,
    description=__description__,
    version=__version__,
    openapi_url="/docs/openapi.json",
    root_path="/llnonebot",
    docs_url=None,
    redoc_url="/docs",
)
api.include_router(api_router, prefix="/api")

app: FastAPI = nonebot.get_app()
app.mount("/llnonebot", app=api)


@driver.on_startup
async def _():
    logger.opt(colors=True).info(
        "LLNoneBot API has served to "
        f"<u><e>http://{driver.config.host}:{driver.config.port}/llnonebot/docs/</e></u>"
    )
