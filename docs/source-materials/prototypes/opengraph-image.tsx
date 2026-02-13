import { ImageResponse } from "next/og";

export const runtime = "edge";

export const alt = "MET4MORFOSES — Anthony James Padavano";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OgImage() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          background: "linear-gradient(135deg, #0a0a0f 0%, #12121a 40%, #0d0d14 100%)",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Accent glow - top left */}
        <div
          style={{
            position: "absolute",
            top: "-120px",
            left: "-80px",
            width: "400px",
            height: "400px",
            borderRadius: "50%",
            background: "radial-gradient(circle, rgba(110,60,200,0.3) 0%, transparent 70%)",
          }}
        />
        {/* Accent glow - bottom right */}
        <div
          style={{
            position: "absolute",
            bottom: "-100px",
            right: "-60px",
            width: "350px",
            height: "350px",
            borderRadius: "50%",
            background: "radial-gradient(circle, rgba(60,180,200,0.25) 0%, transparent 70%)",
          }}
        />

        <p
          style={{
            fontSize: "20px",
            letterSpacing: "6px",
            textTransform: "uppercase",
            color: "rgba(200,200,220,0.5)",
            marginBottom: "12px",
            fontFamily: "sans-serif",
          }}
        >
          MFA Thesis
        </p>
        <h1
          style={{
            fontSize: "72px",
            fontWeight: 700,
            color: "#e8e8f0",
            letterSpacing: "4px",
            margin: 0,
            fontFamily: "sans-serif",
          }}
        >
          MET4MORFOSES
        </h1>
        <p
          style={{
            fontSize: "22px",
            color: "rgba(200,200,220,0.6)",
            marginTop: "16px",
            fontFamily: "sans-serif",
          }}
        >
          Anthony James Padavano
        </p>
      </div>
    ),
    { ...size },
  );
}
