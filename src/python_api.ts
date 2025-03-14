const port = 8008;
const base_url = `http://localhost:${port}`;

class PythonApi {
  async ready() {
    const response = await fetch(`${base_url}`);
    return response.json();
  }

  async shutdown() {
    try {
      await fetch(`${base_url}/shutdown`, {
        signal: AbortSignal.timeout(500)
      });
    } catch (error) {
      console.error(error);
    }
  }
}

const pythonApi = new PythonApi();

export default pythonApi;
