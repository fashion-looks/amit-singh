export type GraphQLError = {
  message: string;
};

export type GraphQLResponse<T> = {
  data?: T;
  errors?: GraphQLError[];
};

/**
 * Minimal browser-side GraphQL helper.
 * Prefer persisted queries for production AEM Publish delivery.
 * The endpoint should be same-origin or explicitly approved by CORS policy.
 */
export async function executeGraphQL<T>(
  endpoint: string,
  query: string,
  variables: Record<string, unknown> = {},
  signal?: AbortSignal
): Promise<T> {
  const response = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ query, variables }),
    credentials: "same-origin",
    signal
  });

  if (!response.ok) {
    throw new Error(`GraphQL request failed: HTTP ${response.status}`);
  }

  const payload = (await response.json()) as GraphQLResponse<T>;

  if (payload.errors?.length) {
    throw new Error(payload.errors.map((item) => item.message).join("; "));
  }

  if (!payload.data) {
    throw new Error("GraphQL response did not contain data.");
  }

  return payload.data;
}
