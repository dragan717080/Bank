from create_app import create_app
from config.assets_config import configure_assets
from helpers import get_blueprints

app = create_app()
configure_assets(app)

for blueprint in get_blueprints():
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug = True)
