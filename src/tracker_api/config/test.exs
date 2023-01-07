import Config

# Configure your database
#
# The MIX_TEST_PARTITION environment variable can be used
# to provide built-in test partitioning in CI environment.
# Run `mix help test` for more information.
config :tracker_api, TrackerAPI.Repo,
  username: "postgres",
  password: "postgres",
  hostname: "localhost",
  database: "tracker_api_test#{System.get_env("MIX_TEST_PARTITION")}",
  pool: Ecto.Adapters.SQL.Sandbox,
  pool_size: 10

# We don't run a server during test. If one is required,
# you can enable the server option below.
config :tracker_api, TrackerAPIWeb.Endpoint,
  http: [ip: {127, 0, 0, 1}, port: 4002],
  secret_key_base: "FVXPhxFCp3sEn0OL47NOqQe9O1qPKAmKRtKeWbB62bEd9vB18UqY2XXCV8tRfUyV",
  server: false

# In test we don't send emails.
config :tracker_api, TrackerAPI.Mailer, adapter: Swoosh.Adapters.Test

# Print only warnings and errors during test
config :logger, level: :warn

# Initialize plugs at runtime for faster test compilation
config :phoenix, :plug_init_mode, :runtime
