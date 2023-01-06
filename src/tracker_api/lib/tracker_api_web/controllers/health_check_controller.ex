defmodule TrackerAPIWeb.HealthCheckController do
    use TrackerAPIWeb, :controller
  
    def show(conn, _params) do
        json(conn, %{health_check: "ok"})
    end
  end